import subprocess
import sys
import os
import time

def main():
    bin_path = sys.argv[1]
    out_path = "/shared/output"
    inp_path = "/home/omer/inp"
    print("Running fuzzing for path={}...".format(bin_path))

    os.environ['AFL_NO_UI'] = '1'

    fuzzer1_env = os.environ.copy()
    fuzzer1_env['AFL_COMPCOV_LEVEL']='2'
    fuzzer1_command = ["/AFLplusplus/afl-fuzz", '-Q', '-p', 'explore', '-c', '0', '-i', inp_path, '-o', out_path, '-M', 'fuzzer01', '--', bin_path]
    fuzzer1 = subprocess.Popen(fuzzer1_command, env=fuzzer1_env)

    fuzzer2_env = os.environ.copy()
    fuzzer2_env['AFL_USE_QASAN']='1'
    fuzzer2_command = ["/AFLplusplus/afl-fuzz", '-Q', '-p', 'explore', '-i', inp_path, '-o', out_path, '-S', 'fuzzer02', '--', bin_path]
    fuzzer2 = subprocess.Popen(fuzzer2_command, env=fuzzer2_env)

    fuzzer3_env = os.environ.copy()
    fuzzer3_env['AFL_PRELOAD']='/AFLplusplus/libcompcov.so'
    fuzzer3_env['AFL_COMPCOV_LEVEL']='2'
    fuzzer3_command = ["/AFLplusplus/afl-fuzz", '-Q', '-p', 'explore', '-i', inp_path, '-o', out_path, '-S', 'fuzzer03', '--', bin_path]
    fuzzer3 = subprocess.Popen(fuzzer3_command, env=fuzzer3_env)


    time.sleep(3)

    while True:
        # subprocess.run(["/AFLplusplus/afl-whatsup", out_path])
        time.sleep(10)

if __name__ == "__main__":
    main()