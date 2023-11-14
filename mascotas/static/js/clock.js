const time = document.getElementById('time');
const date = document.getElementById('date');

const nombreMeses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];

const interval = setInterval(() => {

    const local = new Date();
    let day = local.getDate(),
        month = local.getMonth(),
        year = local.getFullYear();

    time.innerHTML = local.toLocaleTimeString();
    date.innerHTML = `${day} ${nombreMeses[month]} ${year}`;
},1000);