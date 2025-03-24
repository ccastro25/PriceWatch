package com.java.Price_Watch;

import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ProductConfig {
    @Autowired 
    private ProductService service;

    @PostConstruct
    public void setup(){
        service.create(new Product(null, "Milk", 3.33));
    }
}
