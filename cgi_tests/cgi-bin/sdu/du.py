#!/usr/bin/env python3
import cgi
import shutil

from .PartInfo import PartInfo
from .printer.PrinterConsole import PrinterConsole
from .printer.PrinterHtml import PrinterHtml

MOUNT_FILE = "/proc/self/mounts"



def get_partitions_linux():
    result = []
    with open(MOUNT_FILE, "r") as fd:
        for line in fd.readlines():
            if line.startswith("/dev"):
                ldata = line.split(" ")
                row = PartInfo(ldata[0], ldata[1], ldata[2])
                result.append(row)

    return result





# /**
#  * форматирование размера
#  * @param  [int] $bytes
#  * @return [string]
#  */
# function formatSize( $bytes ){
# 		$types = array( 'B', 'KB', 'MB', 'GB', 'TB' );
# 		for( $i = 0; $bytes >= 1024 && $i < ( count( $types ) -1 ); $bytes /= 1024, $i++ );
# 				return( round( $bytes, 2 ) . " " . $types[$i] );
# }


# /**
#  * получить статистику по использованию
#  * @param  [array] $part_struct
#  * @return [array]
#  */
# def get_stat(part: PartInfo):
    
#     total, used, free = shutil.disk_usage(part.mount)

#     part.total = total
#     part.used = used
#     part.free = free


    # print("Total: %d GiB" % (total // (2**30)))
    # print("Used: %d GiB" % (used // (2**30)))
    # print("Free: %d GiB" % (free // (2**30)))


# 	$mount_point = $part_struct["mount"];
# 	/* get disk space free (in bytes) */
# 	$df = disk_free_space($mount_point);
# 	/* and get disk space total (in bytes)  */
# 	$dt = disk_total_space($mount_point);
# 	/* now we calculate the disk space used (in bytes) */
# 	$du = $dt - $df;
# 	/* percentage of disk used - this will be used to also set the width % of the progress bar */
# 	$dp = sprintf('%.2f',($du / $dt) * 100);

# 	$part_struct["free"] = formatSize($df);
# 	$part_struct["total"] = formatSize($dt);
# 	$part_struct["used"] = formatSize($du);
# 	$part_struct["used_prc"] = $dp;

# 	return $part_struct;
# }




def main_app():
    #--- start -------------------------------------------------------------------

    # //--- получаем список разделов
    # if (OS == "Windows") {
    #     $parts = get_partitions_windows($VOLUMES);
    # } else {
    # 	$parts = get_partitions_linux();
    # }

    parts = get_partitions_linux();



    # //--- для каждого раздела вычисляем статистику
    # $items = array();
    # foreach ($parts as $part) {
    # 	$result = get_stat($part);
    # 	array_push($items, $result);
    # }



    text1 = "t1"
    text2 = "t2"
    # form = cgi.FieldStorage()
    # text1 = form.getfirst("TEXT_1", "не задано")
    # text2 = form.getfirst("TEXT_2", "не задано")

    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Du</title>
                <style type='text/css'>

            .progress {
                    border: 2px solid #5E96E4;
                    height: 32px;
                    width: 540px;
                    margin: 30px auto;
            }
            .progress .prgbar {
                    background: #A7C6FF;
                    
                    position: relative;
                    height: 32px;
                    z-index: 999;
            }
            .progress .prgtext {
                    color: #286692;
                    text-align: center;
                    font-size: 13px;
                    padding: 9px 0 0;
                    width: 540px;
                    position: absolute;
                    z-index: 1000;
            }
            .progress .prginfo {
                    margin: 3px 0;
            }

            .title{
                width: 540px;
                margin: 13px auto;
                /*margin-bottom: 20px;*/
                /*text-align: center;*/
            }


            .pitem{
                border: 2px solid #5E96E4;
                margin: 10px auto;
                width: 600px;
            }

        </style>
            </head>
            <body>
            
            <h1 style="text-align: center;">Использование дискового пространства - TODO: OS</h1>
            
            
            """)

    print("<div>")


    Printer = PrinterConsole
    Printer = PrinterHtml


    for part in parts:
        # get_stat(part)
        # print(format_part(part))
        printer = Printer()
        printer.print_info(part)
    print("</div>")
    print("""

    <p>
            v TODO: VERSION
        </p>

    </body>
            </html>""")





if __name__ == "__main__":
    main_app()