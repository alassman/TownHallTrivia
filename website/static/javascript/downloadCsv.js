class TableCSVExporter {
    constructor (table, includeHeaders = false) {
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
        const csvLines = [];
        csvLines.push(this.headerRow);

        for (const answers of this.rows) {
            let cleansedAnswers = [];

            for (let i = 0; i < this.numColumns; i++) {
                if (answers[i] !== undefined) {
                    cleansedAnswers.push(TableCSVExporter.parseCell(answers[i]));
                }
                else {
                  cleansedAnswers.push("Couldn't Read Answer");
                }
            }

            let csvLine = cleansedAnswers.join();
            csvLines.push(csvLine);
        }

        return csvLines.join("\n");
    }

    static parseCell (tableCell) {
        let parsedValue = tableCell;

        // Replace all double quotes with two double quotes
        // parsedValue = parsedValue.replace(/"/g, `""`);

        // If value contains comma, new-line or double-quote, enclose in double quotes
        // parsedValue = /[",\n]/.test(parsedValue) ? `"${parsedValue}"` : parsedValue;
        parsedValue = `"${parsedValue}"`;

        return parsedValue;
    }
}

function download_csv(form) {
  table = [];
  headerRow = [];
  headerRow.push("Timestamp");
  for (let i = 1; i < 7; i++) {
    headerRow.push("Question " + i.toString());
  }
  var data = [new Date(), form.Question1.value, form.Question2.value,form.Question3.value,
              form.Question4.value, form.Question5.value, form.Question6.value];
  table.push(headerRow);
  table.push(data);
  // data.forEach(function(row) {
  //         csv += row.join(',');
  //         csv += "\n";
  // });
  const exporter = new TableCSVExporter(table);
  const csvOutput = exporter.convertToCSV();
  console.log(csvOutput);

  var hiddenElement = document.createElement('a');
  hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csvOutput);
  hiddenElement.target = '_blank';
  hiddenElement.download = form.TeamName.value + '.csv';
  hiddenElement.click();
}