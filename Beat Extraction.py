import librosa

audio_file, sample_rate = librosa.load('song.wav', sr=None)
oenv = librosa.onset.onset_strength(audio_file, sr=sample_rate)
tempo, beat_frames = librosa.beat.beat_track(onset_envelope=oenv, sr=sample_rate)
beat_time = librosa.frames_to_time(beat_frames,sr=sample_rate)
timestamps = []
beat_strengths = oenv[beat_frames]
for i in range(0, len(beat_frames)) :
    if beat_strengths[i] > 6.8475 :
        timestamps.append(beat_time[i])
with open('tempo.txt', 'w') as f:
    for timestamp in timestamps :
        f.writelines(f'{timestamp:.3f}\n')


