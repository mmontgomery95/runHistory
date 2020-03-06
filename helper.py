import sqlite3
import datetime
import inspect

DB_PATH = "/home/mlmont/work/runHistory/fileList.db"
SUCCESS = "Successful run"
FAIL = "Failure to run"


# check if filename exists in list table
# if not, add filename
def add_file():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # receive name of file calling method
        stack = inspect.stack()
        previous_stack_frame = stack[1]
        FILE = previous_stack_frame.filename.split(".")[0].upper()

        # retrieve data from table
        c.execute("SELECT * FROM list")
        rows = c.fetchall()

        # convert to list to search for filename
        out = [item for t in rows for item in t]
        if FILE in out:
            print("File already exists in database")
            pass
        else:
            c.execute(
                "insert into List(filename, status) values(?,?)", (FILE, "active")
            )
            print("Added to list database")
        conn.commit()

    except Exception as e:
        print("Error: ", e)


# add a successful run to the history table
def record_success():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        stack = inspect.stack()
        previous_stack_frame = stack[1]
        FILE = previous_stack_frame.filename.split(".")[0].upper()
        TIME = datetime.datetime.now()
        c.execute(
            "insert into History(Time, Filename, Result) values(?,?,?)",
            (TIME, FILE, SUCCESS),
        )
        conn.commit()
    except Exception as e:
        print("Error: ", e)
        pass


# add unsuccessful run to history table
def record_fail():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        # FILE = os.path.basename(__file__)
        stack = inspect.stack()
        previous_stack_frame = stack[1]
        FILE = previous_stack_frame.filename.split(".")[0].upper()
        TIME = datetime.datetime.now()
        c.execute(
            "insert into history(time, filename, result) values(?,?,?)",
            (TIME, FILE, FAIL),
        )
        conn.commit()
    except Exception as e:
        print("Error: ", e)
