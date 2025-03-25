package com.java.Price_Watch.controller;

import com.java.Price_Watch.model.CVSProduct;
import com.java.Price_Watch.service.StoreProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/cvs")
@CrossOrigin(origins = "*")
public class CVSProductController {

    private final StoreProductService storeProductService;

    @Autowired
    public CVSProductController(StoreProductService storeProductService) {
        this.storeProductService = storeProductService;
    }

    @PostMapping("/products")
    public ResponseEntity<CVSProduct> createProduct(@RequestParam String productName, @RequestParam double price) {
        return ResponseEntity.ok(storeProductService.saveCVSProduct(productName, price));
    }

    @GetMapping("/products")
    public ResponseEntity<List<CVSProduct>> getAllProducts() {
        return ResponseEntity.ok(storeProductService.getAllCVSProducts());
    }

    @GetMapping("/products/{id}")
    public ResponseEntity<CVSProduct> getProductById(@PathVariable Long id) {
        return ResponseEntity.ok(storeProductService.getCVSProductById(id));
    }

    @PutMapping("/products/{id}")
    public ResponseEntity<CVSProduct> updateProduct(@PathVariable Long id, 
                                                  @RequestParam String productName, 
                                                  @RequestParam double price) {
        return ResponseEntity.ok(storeProductService.updateCVSProduct(id, productName, price));
    }

    @DeleteMapping("/products/{id}")
    public ResponseEntity<Void> deleteProduct(@PathVariable Long id) {
        storeProductService.deleteCVSProduct(id);
        return ResponseEntity.ok().build();
    }
} 