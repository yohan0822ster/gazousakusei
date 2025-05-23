"""
This script replicates the functionality of the Perl script gazou.pl.
It provides different modes to generate text files with specific formats
for image galleries or tables.
"""

def main():
    """
    Main function to drive the script.
    It prompts the user for a mode and then executes the corresponding logic.
    """
    # Prompt the user to select a mode.
    mode = input("通常形式複数個なら「y」を。colspanなら「x」を。テーブルなら「t」を：")

    if mode == 'y':
        # Mode 'y': Normal format, multiple items.
        # This mode generates a list of images, each centered.
        total_items = int(input("全個数を入力："))
        # Open gazou.txt for writing with UTF-8 encoding.
        with open("gazou.txt", "w", encoding="utf-8") as f:
            # Loop through the specified number of items.
            for a in range(1, total_items + 1):
                # Format image numbers with leading zeros (e.g., 001, 010).
                if a < 10:
                    f.write("|photo_center\n")
                    f.write(f"|I@00{a}.jpg,▲▲▲|\n\n")
                else:
                    f.write("|photo_center\n")
                    f.write(f"|I@0{a}.jpg,▲▲▲|\n\n")
    elif mode == 'x':
        # Mode 'x': Colspan format.
        # This mode generates a single row of images, potentially for a colspan layout.
        horizontal_items = int(input("横の個数を入力："))
        # Open gazou.txt for writing with UTF-8 encoding.
        with open("gazou.txt", "w", encoding="utf-8") as f:
            f.write("|photo_center\n")
            if horizontal_items == 1:
                # Special case for a single item.
                f.write("|I@001.jpg,▲▲▲|\n") # In Perl, this was I@001.jpg, so kept 1-indexed.
            else:
                # Build a line with multiple image references.
                image_line = ""
                for i in range(horizontal_items): # 0-based indexing for multiple items.
                    # Format image numbers with leading zeros.
                    if i < 10:
                         image_line += f"|I@00{i}.jpg"
                    else:
                         image_line += f"|I@0{i}.jpg"
                image_line += "|\n"
                f.write(image_line)
                f.write("|M@▲▲▲|\n") # Common caption for the row.
    elif mode == 't':
        # Mode 't': Table format.
        # This mode generates an HTML table structure.
        vertical_items = int(input("縦の個数を入力："))
        horizontal_items = int(input("横の個数を入力："))
        # Open table.txt for writing with UTF-8 encoding.
        with open("table.txt", "w", encoding="utf-8") as f:
            # Write the opening HTML table tags.
            f.write('<div><table class="Table1" border="0" cellPadding="0" cellSpacing="1" >\n')
            # Loop for each row.
            for a in range(vertical_items):
                f.write("<tr>\n<th>data</th>") # First cell is a header.
                # Loop for subsequent cells in the row.
                for b in range(1, horizontal_items):
                    f.write("<td>")
                    f.write("data") # Placeholder data.
                    f.write("</td>\n")
                f.write("</tr>\n")
            # Write the closing HTML table tags.
            f.write("</table></div>\n")
    else:
        # Invalid Mode: If the user input doesn't match 'y', 'x', or 't'.
        print("end")

if __name__ == "__main__":
    # Execute the main function when the script is run directly.
    main()
