// Fetch products and render them on the page
document.addEventListener("DOMContentLoaded", function() {
    const loadButton = document.getElementById("load-products");
    const productList = document.getElementById("product-list");

    if (loadButton) {
        loadButton.addEventListener("click", function() {
            fetch("/api/products")
                .then(response => response.json())
                .then(data => {
                    productList.innerHTML = ""; // Clear the previous list
                    data.products.forEach(product => {
                        const item = document.createElement("li");
                        item.textContent = `${product.title}: ${product.description}`;
                        productList.appendChild(item);
                    });
                })
                .catch(error => console.error("Error fetching products:", error));
        });
    }
});
