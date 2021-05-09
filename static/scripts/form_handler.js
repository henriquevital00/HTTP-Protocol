const form = document.getElementById("publications-form");

$(document).ready(_ => fetchPublications());


form.addEventListener("submit", e => {
    e.preventDefault();

    formData = new FormData(e.target);
    result_data = FormDatatoJson(formData);

    sendPublication(result_data)
});

$(function() {
    $("#file-form").submit(async (e) => {
        e.preventDefault(); 

        const formData = new FormData(e.target);

        const file = formData.get("file");
        let bytes = await to_base64_string(file);
        bytes = bytes.split("base64,")[1]

        $("#file_sent_warning").html(
            `<div class='alert alert-secondary'>
                Criando o arquivo ${file.name}...
            </div>`
        )

        $.ajax({
            type: "PUT",
            url: `http://localhost:8000/${file.name}`,
            data: bytes, 
            success: () => {
                $("#file_sent_warning").html(
                    `<div class='alert alert-success'>
                        Arquivo ${file.name} criado
                    </div>`
                )
            },
            error: () => {
                $("#file_sent_warning").html(
                    `<div class='alert alert-danger'>
                        Erro ao criar o arquivo ${file.name}
                    </div>`
                )
            }
        })
    });
});


