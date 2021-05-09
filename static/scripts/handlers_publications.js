const fetchPublications = async () => {

    let response = await fetch("http://localhost:8000/publications/all", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        method: "GET",
    });

    response = await response.json();

    mountPublicationCard(response);
};

const deletePublication = async (id) => {

    let response = await fetch(`http://localhost:8000/publications/${id}`,{
        headers: {
            'Accept': 'application/json',
        },
        method: "DELETE"
    });

    response = await response.json();
    mountPublicationCard(response);
};

const sendPublication = async (data) => {

    let response = await fetch("http://localhost:8000/publications/create",{
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "POST",
        body: data
    });

    response = await response.json();

    mountPublicationCard(response);
};

const mountPublicationCard = response => {

    response = response.reverse().map(resp => 
        `<div class="publication-card mt-4">
            <h1>${resp.hashtag}</h1>
            <p>${resp.content}</p>
            <p>${toDateString(resp.date)}</p>
            <button class="btn btn-danger" onClick={deletePublication(${resp.id})}>Deletar</button>
        </div>`
    );
    
    $("#posts").html(response.join(''));
};

