import Collect
import Process
import Doc

if __name__ == "__main__":
    Collect.Paths.changeDate('2023-09-10')
    videoNum = Collect.getData()
    Process.process()
    Doc.makeDoc(videoNum, False)
