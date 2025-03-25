package com.java.Price_Watch.controller;

import com.java.Price_Watch.model.RiteAidProduct;
import com.java.Price_Watch.service.StoreProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/riteaid")
@CrossOrigin(origins = "*")
public class RiteAidProductController {

    private final StoreProductService storeProductService;

    @Autowired
    public RiteAidProductController(StoreProductService storeProductService) {
        this.storeProductService = storeProductService;
    }

    @PostMapping("/products")
    public ResponseEntity<RiteAidProduct> createProduct(@RequestParam String productName, @RequestParam double price) {
        return ResponseEntity.ok(storeProductService.saveRiteAidProduct(productName, price));
    }

    @GetMapping("/products")
    public ResponseEntity<List<RiteAidProduct>> getAllProducts() {
        return ResponseEntity.ok(storeProductService.getAllRiteAidProducts());
    }

    @GetMapping("/products/{id}")
    public ResponseEntity<RiteAidProduct> getProductById(@PathVariable Long id) {
        return ResponseEntity.ok(storeProductService.getRiteAidProductById(id));
    }

    @PutMapping("/products/{id}")
    public ResponseEntity<RiteAidProduct> updateProduct(@PathVariable Long id, 
                                                      @RequestParam String productName, 
                                                      @RequestParam double price) {
        return ResponseEntity.ok(storeProductService.updateRiteAidProduct(id, productName, price));
    }

    @DeleteMapping("/products/{id}")
    public ResponseEntity<Void> deleteProduct(@PathVariable Long id) {
        storeProductService.deleteRiteAidProduct(id);
        return ResponseEntity.ok().build();
    }
} 