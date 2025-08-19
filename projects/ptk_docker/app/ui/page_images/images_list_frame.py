import tkinter as tk
from enum import Enum
from tkinter import ttk


class Column(Enum):
    repository = "repository"
    tag = "tag"
    image_id = "image_id"
    crated = "created"
    size = "size"


class ImagesListFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        tree_columns: list[Column] = [
            Column.repository,
            Column.tag,
            Column.image_id,
            Column.crated,
            Column.size,
        ]
        self._tree = ttk.Treeview(
            self,
            show="tree headings",
            selectmode="browse",
            columns=[c.value for c in tree_columns],
        )

        self._tree.pack(side="left", expand=True, fill="both")

        self._tree.heading("#0", text="id")
        for c in tree_columns:
            self._tree.heading(c.value, text=c.value)
        # self._tree.heading("size", text="Size")

        # self._tree.column("#0", minwidth=200, width=200)
        # self._tree.column("id", minwidth=90, width=90)

        # vertical scroll
        ysb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        self._tree["yscroll"] = ysb.set
        ysb.pack(side="right", expand=False, fill="y", anchor="e")

        # self._tree.column("#0", width=300)
        # self._tree.tag_bind("simple", "<<TreeviewSelect>>", self._select_row)
        # self._tree.bind("<Double-1>", self._open_row)
        # self._tree.tag_bind("simple", "<<TreeviewOpen>>", self.__open_row)
        # self._tree.bind("<Button-3>", self._make_cmenu)

        # self.cmenu = tk.Menu(self, tearoff=0)
        # self.cmenu.add_command(
        #     label="Свойства",
        #     command=self._show_info,
        #     # image=ticons.ticon(ticons.INFO),
        #     compound="left",
        # )
        # self.cmenu.add_command(label="Экспорт", command=self.__show_export, image=ticons.ticon(ticons.I_EXPORT), compound="left")
        # self.cmenu.add_command(
        #     label="Удалить",
        #     command=self._show_remove,
        #     # image=ticons.ticon(ticons.TRASH),
        #     compound="left",
        # )

    def set_images(self, images):
        # clear
        for row in self._tree.get_children():
            self._tree.delete(row)

        for img in images:
            # pprint.pprint(img.attrs)

            ivalues = (
                img.tags[0] if img.tags else "-",
                # "\n".join(img.tags),
                img.attrs.get("Size", 0),
            )

            self._tree.insert(
                "",
                "end",
                img.short_id,
                text=img.short_id,
                # tags=("simple",),
                # image=icon,
                values=ivalues,
            )


"""

func (cf *ImagesFrame) splitTag(full_tag string) (string, string) {
	result := strings.Split(full_tag, ":")

	repo := strings.Join(result[:len(result)-1], ":")
	return repo, result[len(result)-1]
}


---

const ShortImageIDLength = 12

// ShortImageID - конвертирует длинное представление id образа в короткое
// sha256:2503e324e27050f4d3fd21d25147ca108840864941d96097c2633cd9232f5088
// 2503e324e270
func ShortImageID(id string) string {

	split_result := strings.Split(id, ":")

	if len(split_result) != 2 {
		return id
	}

	if len(split_result[1]) < 12 {
		return id
	}

	return split_result[1][:ShortImageIDLength]
}
---



const (
	ONE_KB = 1024
	//  ONE_KB_BI = BigInteger.valueOf(1024L);
	ONE_MB = 1048576
	//   public static final BigInteger ONE_MB_BI;
	ONE_GB = 1073741824
	//   public static final BigInteger ONE_GB_BI;
	ONE_TB = 1099511627776
	//public static final BigInteger ONE_TB_BI;
	ONE_PB = 1125899906842624
	//public static final BigInteger ONE_PB_BI;
	ONE_EB = 1152921504606846976
	//public static final BigInteger ONE_EB_BI;
	// public static final BigInteger ONE_ZB;
	// public static final BigInteger ONE_YB;
)

func ByteCountToDisplaySize(size int64) string {

	// try_eb := size / ONE_EB
	// if try_eb > 0 {
	// 	return fmt.Sprintf("%d EB", try_eb)
	// }

	// try_pb := size / ONE_PB
	// if try_pb > 0 {
	// 	return fmt.Sprintf("%d PB", try_pb)
	// }

	// try_tb := size / ONE_TB
	// if try_tb > 0 {
	// 	return fmt.Sprintf("%d TB", try_tb)
	// }

	try_gb := size / ONE_GB
	if try_gb > 0 {
		return fmt.Sprintf("%d GB", try_gb)
	}

	try_mb := size / ONE_MB
	if try_mb > 0 {
		return fmt.Sprintf("%d MB", try_mb)
	}

	try_kb := size / ONE_KB
	if try_kb > 0 {
		return fmt.Sprintf("%d KB", try_kb)
	}

	// Objects.requireNonNull(size, "size");
	// String displaySize;
	// if (size.divide(ONE_EB_BI).compareTo(BigInteger.ZERO) > 0) {
	//    displaySize = size.divide(ONE_EB_BI) + " EB";
	// } else if (size.divide(ONE_PB_BI).compareTo(BigInteger.ZERO) > 0) {
	//    displaySize = size.divide(ONE_PB_BI) + " PB";
	// } else if (size.divide(ONE_TB_BI).compareTo(BigInteger.ZERO) > 0) {
	//    displaySize = size.divide(ONE_TB_BI) + " TB";
	// } else if (size.divide(ONE_GB_BI).compareTo(BigInteger.ZERO) > 0) {
	//    displaySize = size.divide(ONE_GB_BI) + " GB";
	// } else if (size.divide(ONE_MB_BI).compareTo(BigInteger.ZERO) > 0) {
	//    displaySize = size.divide(ONE_MB_BI) + " MB";
	// } else if (size.divide(ONE_KB_BI).compareTo(BigInteger.ZERO) > 0) {
	//    displaySize = size.divide(ONE_KB_BI) + " KB";
	// } else {
	//    displaySize = size + " bytes";
	// }

	return fmt.Sprintf("%d bytes", size)
}
"""
