import shutil

class PartInfo:
    def __init__(self, dev, mount, fs):
        self.dev = dev
        self.mount = mount
        self.fs = fs

        self.free = 0
        self.total = 0
        self.used = 0
        self.used_prc = 0

        #--- start
        self.__fill()

    def __fill(self):
        total, used, free = shutil.disk_usage(self.mount)

        self.total = total
        self.used = used
        self.free = free


        # print("Total: %d GiB" % (total // (2**30)))
        # print("Used: %d GiB" % (used // (2**30)))
        # print("Free: %d GiB" % (free // (2**30)))

    @staticmethod
    def format_size(v: int):
        # function formatSize( $bytes ){
        # 		$types = array( 'B', 'KB', 'MB', 'GB', 'TB' );
        # 		for( $i = 0; $bytes >= 1024 && $i < ( count( $types ) -1 ); $bytes /= 1024, $i++ );
        # 				return( round( $bytes, 2 ) . " " . $types[$i] );
        # }
        return v