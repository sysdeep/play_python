from ..PartInfo import PartInfo
from .PrinterInterface import PrinterInterface

class PrinterHtml(PrinterInterface):
    def __init__(self):
        pass

    def print_info(self, part: PartInfo):

        

        
        tpl = f"""
        <div class="pitem">

	
            <div class="title">

                <h4>
                    {part.dev}
                    <span style='float: right;'>{part.mount}</span>
                </h4>
            </div>


            <div class='progress'>
                <div class='prgtext'>{part.used_prc}% Использовано</div>
                <div class='prgbar' style="width: {part.used_prc}%"></div>
                <div class='prginfo'>
                        <span style='float: left;'>
                            использовано 
                                <strong>
                                    {part.used}
                                </strong> 
                            из 
                                <strong>{part.total}</strong>
                        <span style='float: right;'>
                            свободно <strong>{part.free}</strong> 
                            из 
                            <strong>{part.total}</strong>
                        <span style='clear: both;'></span>
                </div>
            </div>

        </div>
        """

        print(tpl)