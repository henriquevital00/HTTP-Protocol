const form = document.getElementById("publications-form");

$(document).ready(_ => fetchPublications());


form.addEventListener("submit", e => {
    e.preventDefault();

    formData = new FormData(e.target);
    result_data = FormDatatoJson(formData);

    sendPublication(result_data)
});

$(function() {
    $("#testForm").submit(async (e) => {
        e.preventDefault(); 

        const formData = new FormData(e.target);

        const file = formData.get("thumb");
        const bytes = await to_base64_string(file);
        
        const data = JSON.stringify({
            fileName: file.name,
            byteContent: bytes
        });

        console.log(data)

        $.ajax({
            type: "PUT",
            url: "http://localhost:8000",
            data: data, 
            success: function(data){
                alert(data); 
            }
        })
    });
})


