$(document).ready(function() {
    $('.select2').select2({
        placeholder: "Search...",
        allowClear: true,
        width: '100%'
    });

    // Handle medicine selection and modal display
    $('#medicinesDropdown').on('select2:select', function(e) {
        const selectedText = $(this).find("option:selected").text();
        $('#medicineName').val(selectedText);
        $('#medicineDetailsModal').modal('show');
    });

    // Handle lab test selection and update textarea
    $('#labTestsDropdown').on('select2:select', function(e) {
        const selectedText = $(this).find("option:selected").text();
        const labTestEntry = `Lab Test: ${selectedText}`;
        $('#labTestsTextArea').append(labTestEntry + '\n');
    });

    // Handle adding medicine to prescription
    $('#addMedicineButton').on('click', function() {
        const medicineName = $('#medicineName').val();
        const doseMorning = $('#doseMorning').is(':checked');
        const doseAfternoon = $('#doseAfternoon').is(':checked');
        const doseEvening = $('#doseEvening').is(':checked');
        const doseNight = $('#doseNight').is(':checked');
        const doseAmount = $('#doseAmount').val();
        const rowCount = $('#medicinesTableBody tr').length + 1;

        const newRow = `
            <tr>
                <td>${rowCount}</td>
                <td>${medicineName}</td>
                <td>${doseAmount}</td>
                <td>${doseMorning ? '✔️' : ''}</td>
                <td>${doseAfternoon ? '✔️' : ''}</td>
                <td>${doseEvening ? '✔️' : ''}</td>
                <td>${doseNight ? '✔️' : ''}</td>
            </tr>
        `;
        $('#medicinesTableBody').append(newRow);
        $('#medicineDetailsModal').modal('hide');
    });
});

function printPrescription() {
    const labTestsContent = document.getElementById('labTestsTextArea').value;
    const medicinesContent = document.getElementById('medicinesTableBody').innerHTML;
    const printWindow = window.open('', '', 'height=600,width=800');
    printWindow.document.write('<html><head><title>Prescription</title></head><body>');
    printWindow.document.write('<h3>Lab Tests</h3>');
    printWindow.document.write('<pre>' + labTestsContent + '</pre>');
    printWindow.document.write('<h3>Medicines</h3>');
    printWindow.document.write('<table border="1">' + medicinesContent + '</table>');
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();
}
