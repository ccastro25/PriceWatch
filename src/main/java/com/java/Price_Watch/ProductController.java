package com.java.Price_Watch;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins ="*")
@RestController
@RequestMapping(value="/productController")
public class ProductController {
    private ProductService service;

    @Autowired
    public ProductController(ProductService service){
        this.service = service;
    }

    @PostMapping(value = "/create")
    public ResponseEntity<Product> create(@RequestBody Product product){
        System.out.println("hellow");
        Product newProduct = service.create(product);
        return new ResponseEntity<>(newProduct, HttpStatus.OK);
    }

    @GetMapping(value = "/read/{productID}")
    public ResponseEntity<Product> readById(@PathVariable Long productID){
        Product productINDB = service.readById(productID);
        return new ResponseEntity<>(productINDB, HttpStatus.OK);
    }

    @GetMapping(value ="/readAll")
    public ResponseEntity<List<Product>> readAll(){
        return new ResponseEntity<>(service.readAll(),HttpStatus.OK);
    }
    
    @PutMapping(value = "/update/{productID}")
    public ResponseEntity<Product> update(@PathVariable Long productID,@RequestBody Product newDataForProduct ){
        return new ResponseEntity<>(service.update(productID,newDataForProduct),HttpStatus.OK);
    }

    @DeleteMapping(value = "/delete/{id}")
    public ResponseEntity<Product> delete(@PathVariable Long id){
        return new ResponseEntity<>(service.delete(id),HttpStatus.OK);
    }
}
