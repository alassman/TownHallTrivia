function download_csv(form) {
  console.log(data)
  var data = [form.Question1.value, form.Question2.value, form.Question3.value,
              form.Question4.value, form.Question5.value, form.Question6.value];
  var csv = 'Question1,Question2,Question3,Question4,Question5,Question6\n';
  // data.forEach(function(row) {
  //         csv += row.join(',');
  //         csv += "\n";
  // });
  csv += data.join(',');
  console.log(csv);
  var hiddenElement = document.createElement('a');
  hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
  hiddenElement.target = '_blank';
  hiddenElement.download = form.TeamName.value + '.csv';
  hiddenElement.click();
}