package com.java.Price_Watch;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ProductService {
    private ProductRepository   repository;

    @Autowired
    public ProductService(ProductRepository repository){
        this.repository = repository;
    }

    public Product create(Product product){
        Product productInDB = repository.save(product);
        return productInDB;
    }

    public Product readById(Long id){
        return repository.findById(id).get();
    }

    public List<Product> readAll(){
        Iterable<Product> iterable = repository.findAll();
        List<Product> productList = new ArrayList<>();
        iterable.forEach(productList::add);
        return productList;
    }

    public Product update(Long productID, Product dataToPersist){
        Product productIdInDB = this.readById(productID);
        productIdInDB.setPrice(dataToPersist.getPrice());
        productIdInDB.setProductName(dataToPersist.getProductName());
        productIdInDB = repository.save(productIdInDB);
        return productIdInDB;
    }

    public Product delete(Long productID){
        Product productToDelete =this.readById(productID);
        repository.delete(productToDelete);
        return productToDelete;
    }
}
