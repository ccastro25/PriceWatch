async function getDBInfo() {
    try {
        let searchProduct = document.getElementById('searchInput').value;
        let selectedStores = Array.from(document.querySelectorAll('input[name="store"]:checked'))
            .map(checkbox => checkbox.value);
        
        if (selectedStores.length === 0) {
            alert('Please select at least one store to compare');
            return;
        }

        let results = [];
        
        // Fetch data from each selected store
        for (let store of selectedStores) {
            let url = `http://localhost:9007/api/${store}/products`;
            const response = await fetch(url);
            const storeProducts = await response.json();
            
            // Filter products by search term and add store name
            let matchingProducts = storeProducts
                .filter(product => product.productName.toLowerCase().includes(searchProduct.toLowerCase()))
                .map(product => ({
                    ...product,
                    store: store.charAt(0).toUpperCase() + store.slice(1)
                }));
            
            results = results.concat(matchingProducts);
        }

        // Sort results by price
        results.sort((a, b) => a.price - b.price);
        
        // Display results
        displayResults(results);
    } catch (error) {
        console.error("Error:", error);
        alert('Error fetching product data. Please try again.');
    }
}

function displayResults(results) {
    let container = document.getElementById("table");
    
    // Clear previous results
    if (container.childNodes.length > 0) {
        container.removeChild(container.firstElementChild);
    }

    // Create table
    let table = document.createElement("table");
    
    // Create header
    let thead = document.createElement("thead");
    let headerRow = document.createElement("tr");
    
    // Add headers
    ["Store", "Product Name", "Price", "Date"].forEach(header => {
        let th = document.createElement("th");
        th.innerText = header;
        headerRow.appendChild(th);
    });
    
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create body
    let tbody = document.createElement("tbody");
    
    // Add rows
    results.forEach(product => {
        let row = document.createElement("tr");
        
        // Add cells
        [product.store, product.productName, `$${product.price.toFixed(2)}`, product.date].forEach(value => {
            let cell = document.createElement("td");
            cell.innerText = value;
            row.appendChild(cell);
        });
        
        tbody.appendChild(row);
    });
    
    table.appendChild(tbody);
    container.appendChild(table);
}


