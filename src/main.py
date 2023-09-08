import Collect
import Process
import Doc

if __name__ == "__main__":
    videoNum = Collect.getData()
    #Process.paths.changeDate('2023-08-25')
    Process.process()
    Doc.makeDoc(videoNum, False)
