function create()
{
    var str = Document.getElementByID("input");
    var regex = /^[A-Za-z]$/;

    if(!regex.test(str))
    {
        alert("Cannot include numbers");
    }
}