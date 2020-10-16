with open("input.txt", encoding="utf-8") as cin:
    cmd = cin.readline()
    cmd = cmd.replace('^', '')
    for num in range(int(input('Enter episodes start range(inclusive):')), int(input('Enter episodes end range(exclusive):'))):
        exc_cmd = cmd.replace('$', '0' + str(num) if num < 10 else str(num))
        import subprocess
        process = subprocess.Popen(exc_cmd, stdout=subprocess.PIPE)
        while True:
            output = process.stdout.readline()
            print(output.strip())
            # Do something else
            return_code = process.poll()
            if return_code is not None:
                print('RETURN CODE', return_code)
                # Process has finished, read rest of the output 
                for output in process.stdout.readlines():
                    print(output.strip())
                break
import os
os.system("pause")
