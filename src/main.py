import Collect
import Process
import Doc

if __name__ == "__main__":
    videoNum = Collect.getData()
    Process.process()
    Doc.makeDoc(videoNum, False)
