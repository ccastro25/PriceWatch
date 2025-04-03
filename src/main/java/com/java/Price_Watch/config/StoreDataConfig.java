package com.java.Price_Watch.config;

import com.java.Price_Watch.service.StoreProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import jakarta.annotation.PostConstruct;

@Configuration
public class StoreDataConfig {

    private final StoreProductService storeProductService;

    @Autowired
    public StoreDataConfig(StoreProductService storeProductService) {
        this.storeProductService = storeProductService;
    }

    @PostConstruct
    public void setup() {
        // CVS Sample Data
        storeProductService.saveCVSProduct("Milk", 4.29);
        storeProductService.saveCVSProduct("Bread", 2.99);
        storeProductService.saveCVSProduct("Eggs", 3.49);
        storeProductService.saveCVSProduct("Butter", 5.29);
        storeProductService.saveCVSProduct("Cheese", 6.49);

        // Walmart Sample Data
        storeProductService.saveWalmartProduct("Milk", 3.99);
        storeProductService.saveWalmartProduct("Bread", 2.49);
        storeProductService.saveWalmartProduct("Eggs", 3.29);
        storeProductService.saveWalmartProduct("Butter", 4.99);
        storeProductService.saveWalmartProduct("Cheese", 5.99);
    }
} 