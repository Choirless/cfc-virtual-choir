import argparse
import warnings

import numpy as np
import librosa
import optuna

# to surpress warning about libaudiofile
warnings.filterwarnings('ignore')


def measure_error(x0, x1, offset):
  max_len = min(len(x0), len(x1))
  diff = x0[:max_len]-np.roll(x1[:max_len], offset)
  err = np.sum(diff**2) / len(diff)
  return err

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Calculate alignment offset for a number of video/audio files')
  parser.add_argument('fn_leader',
                      help='filename of the leader part as reference')
  parser.add_argument('fn_parts', nargs='+',
                      help='one or more filenames of other parts to align to leader')
  parser.add_argument('--sample_rate', type=int, default=1000,
                      help='audio sample rate used')

  args = parser.parse_args()
  fn_leader = args.fn_leader
  fn_parts = args.fn_parts
  sample_rate = args.sample_rate
  
  # Load the leader part
  x0, fs0 = librosa.load(fn_leader, sr=sample_rate, mono=True, duration=20)
  x0 = np.abs((x0 - x0.mean()) / x0.std()) # normalize

  # Check each part in turn
  for fn_part in fn_parts:

    # Load the audio from file
    x1, fs1 = librosa.load(fn_part, sr=sample_rate, mono=True, duration=20)                      

    # Normalize
    x1 = np.abs((x1 - x1.mean()) / x1.std())

    def objective(trial):
      offset = trial.suggest_int('offset', -sample_rate, sample_rate, 100)
      return measure_error(x0, x1, offset)

    # Run the optimisation to find best fit
    study = optuna.create_study()
    study.optimize(objective, n_trials=100, show_progress_bar=True)

    # Calculate offset in milliseconds
    offset = study.best_params['offset']
    offset_ms = (offset / sample_rate) * 1000

    print(f"Offset for: {fn_part} is {offset_ms} ms")

