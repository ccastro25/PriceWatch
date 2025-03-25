package com.java.Price_Watch.controller;

import com.java.Price_Watch.model.WalmartProduct;
import com.java.Price_Watch.service.StoreProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/walmart")
@CrossOrigin(origins = "*")
public class WalmartProductController {

    private final StoreProductService storeProductService;

    @Autowired
    public WalmartProductController(StoreProductService storeProductService) {
        this.storeProductService = storeProductService;
    }

    @PostMapping("/products")
    public ResponseEntity<WalmartProduct> createProduct(@RequestParam String productName, @RequestParam double price) {
        return ResponseEntity.ok(storeProductService.saveWalmartProduct(productName, price));
    }

    @GetMapping("/products")
    public ResponseEntity<List<WalmartProduct>> getAllProducts() {
        return ResponseEntity.ok(storeProductService.getAllWalmartProducts());
    }

    @GetMapping("/products/{id}")
    public ResponseEntity<WalmartProduct> getProductById(@PathVariable Long id) {
        return ResponseEntity.ok(storeProductService.getWalmartProductById(id));
    }

    @PutMapping("/products/{id}")
    public ResponseEntity<WalmartProduct> updateProduct(@PathVariable Long id, 
                                                      @RequestParam String productName, 
                                                      @RequestParam double price) {
        return ResponseEntity.ok(storeProductService.updateWalmartProduct(id, productName, price));
    }

    @DeleteMapping("/products/{id}")
    public ResponseEntity<Void> deleteProduct(@PathVariable Long id) {
        storeProductService.deleteWalmartProduct(id);
        return ResponseEntity.ok().build();
    }
} 