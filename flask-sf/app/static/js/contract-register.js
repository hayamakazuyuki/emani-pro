const openContractorSearch = (url, name) => {
    window.open(url, name, 'width=400, height=350')
}

const selectContractor = () => {

    if(!window.opener || window.opener.closed) {
        window.close();
        return false;
    } else {

        // grab the checkboxes in the document;
        const checkbox = document.querySelectorAll('input[type="checkbox"]');

        for (let i=0; i<checkbox.length; i++) {
            if (checkbox[i].checked) {

                // get selected contractor's ID and name;
                contractor_id = checkbox[i].value;
                contractor_name = document.getElementsByName("contractor_name")[i].innerHTML

                // set values to the parent window;
                window.opener.document.getElementById("contractor_id").value = contractor_id;
                window.opener.document.getElementById("contractor_name").textContent = contractor_name;

                // close the window;
                window.close();
            }
        }
    }
}
