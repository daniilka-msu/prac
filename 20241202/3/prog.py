import struct
import sys

def parse_wav_header():
    data = sys.stdin.buffer.read(44)

    if len(data) < 44:
        print("NO")
        return

    try:
        riff, size, wave, fmt, fmt_length, audio_format, channels, rate, byte_rate, block_align, bits_per_sample, data_marker, data_size = struct.unpack(
            '<4sI4s4sIHHIIHH4sI', data)
    except struct.error:
        print("NO")
        return

    if riff != b'RIFF' or wave != b'WAVE' or fmt != b'fmt ' or data_marker != b'data':
        print("NO")
        return

    header_info = f"Size={size + 8}, Type={audio_format}, Channels={channels}, Rate={rate}, Bits={bits_per_sample}, Data size={data_size}"

    print(header_info)

parse_wav_header()
