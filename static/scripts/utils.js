const FormDatatoJson = formData => {

    let obj = {};
    formData.forEach((value, key) => obj[key] = value);
    obj["date"] = new Date(Date.now()).toISOString()

    return JSON.stringify(obj);
}

const toDateString = date => {

    date = new Date(date);
    
    date = [`${date.getDate()}`.padStart(2, "0"), 
            `${date.getMonth() + 1}`.padStart(2, "0"), 
             date.getFullYear()];
    
    
    return date.join("/");
}
