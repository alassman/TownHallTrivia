class TableCSVExporter {
    constructor (table, includeHeaders = true) {
        this.table = table;
        this.headerRow = [];
        this.rows = table;
        this.numColumns = this.rows[0].length

        if (!includeHeaders && this.rows[0].length) {
          this.headerRow = table[0];
          this.rows.shift();
        }
    }

    convertToCSV() {
        const lines = [];

        for (const row of this.rows) {
            let line = "";

            for (let i = 0; i < this.numColumns; i++) {
                if (row[i] !== undefined) {
                    line += TableCSVExporter.parseCell(row[i]);
                }

                line += (i !== (numCols - 1)) ? "," : "";
            }

            lines.push(line);
        }

        return lines.join("\n");
    }

    static parseCell (tableCell) {
        let parsedValue = tableCell.textContent;
        parsedValue += "\"";


        // Replace all double quotes with two double quotes
        // parsedValue = parsedValue.replace(/"/g, `""`);

        // If value contains comma, new-line or double-quote, enclose in double quotes
        // parsedValue = /[",\n]/.test(parsedValue) ? `"${parsedValue}"` : parsedValue;

        return parsedValue;
    }
}
