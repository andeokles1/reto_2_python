import os


class Pytest:
    path = './db/db_oltp.db'

    def check_database_file(self):
        assert not os.path.isfile(self.path) == True
