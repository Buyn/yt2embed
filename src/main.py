
# ----------------------------------------------
# * imports : 
# ----------------------------------------------
import sys , os


# ----------------------------------------------
# * vars :
# ----------------------------------------------


# ----------------------------------------------
# * main:
# ----------------------------------------------
# ** def main(argv):
# ----------------------------------------------
def main(argv):
    ytid = get_id(argv[1])
    print("ID = ", ytid)
    if ytid != "not found":
        start_cmd(ytid)
    end_app(0)


# ----------------------------------------------
# ** def start_cmd:
# ----------------------------------------------
def start_cmd(arg):
    # run_cmd = "start /wait cmd /c ffe " + arg
    run_cmd = "ffe " + arg
    print(run_cmd)
    os.system(run_cmd)


# ----------------------------------------------
# ** end_app(arg) : 
def end_app(arg):
    sys.exit(arg)


# ----------------------------------------------
# ** get_id(string) : 
def get_id(string):
    r = string.split("/")
    if string.startswith("test"):
        return "test"
    if string.startswith("https://youtu.be/"):
        return r[3]
    return "not found"


# ----------------------------------------------
# ** -------------------------------------------:
# * if __name__ : 
# ----------------------------------------------
if __name__ == "__main__": 
    import sys
    # sys.argv = ['', 'Test.testName']
    main(sys.argv)


# ----------------------------------------------
# * -------------------------------------------:
