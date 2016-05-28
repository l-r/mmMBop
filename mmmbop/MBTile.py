import sqlite3


class MBTile:

    def __init__(self, src, z, x, y):
        self.conn = sqlite3.connect(src)
        self.z = z
        self.x = x
        self.y = y

    def get_data(self):
        # TODO ask a competent person what this does
        self.y = (1 << self.z) - 1 - self.y

        c = self.conn.cursor()
        c.execute(
            '''select tile_data from tiles where zoom_level=%s and tile_column=%s and tile_row=%s''' % (
                self.z, self.x, self.y
            )
        )

        result = c.fetchone()
        return bytes(result[0]) if result else []
