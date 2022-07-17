function csv_ranking_to_table() {
    console.log("Running csv_to_table");
    const table = document.getElementById("csv-table");
    const path = document.getElementById("csv-url").textContent;

    console.log(`Reading csv: ${path}`);
    fetch(path).then(r => r.text()).then(txt => {
        let lines = txt.split("\n");
        lines.forEach((l,i) => {
            let row = document.createElement("tr");

            let rankCell = document.createElement("td");
            rankCell.className = "rankcell";
            rankCell.textContent = i + 1;
            row.appendChild(rankCell);

            sections = l.split("\",\"")
            
            //name
            let nametext = sections[0].replace("\"","");
            let namecell = document.createElement("td");
            namecell.className = `namecell`;
            namecell.textContent = nametext;
            row.appendChild(namecell);

            //source
            let sourcetext = sections[1].replace("\"","");
            let sourcecell = document.createElement("td");
            sourcecell.className = `sourcecell`;
            sourcecell.textContent = sourcetext;
            row.appendChild(sourcecell);

            //link
            let linktext = sections[2];
            let linkcell = document.createElement("td");
            linkcell.className - `linkcell`;
            linkcell.innerHTML = `<a href=${linktext}>Link</a>`;            
            row.appendChild(linkcell);
            
            table.appendChild(row);
        });

    });
}

csv_ranking_to_table();