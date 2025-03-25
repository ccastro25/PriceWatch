package com.java.Price_Watch.model;

import jakarta.persistence.MappedSuperclass;
import jakarta.persistence.Column;
import java.time.LocalDate;

@MappedSuperclass
public abstract class BaseProduct {
    
    @Column(name = "product_name")
    private String productName;
    
    @Column(name = "price")
    private double price;
    
    @Column(name = "date")
    private LocalDate date;

    public BaseProduct() {}

    public BaseProduct(String productName, double price, LocalDate date) {
        this.productName = productName;
        this.price = price;
        this.date = date;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
} 