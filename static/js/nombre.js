document.getElementById('nameForm').addEventListener('submit', function(event){
    event.preventDefault(); // prevent form from submitting normally
    var name = document.getElementById("name").value;
});