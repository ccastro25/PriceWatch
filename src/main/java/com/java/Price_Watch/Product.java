package com.java.Price_Watch;


import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Product {
    
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String productName;
    private double price;

    public Product(){}
    
    public Product(Long id, String productName, double price){
        this.id = id;
        this.productName = productName;
        this.price = price;
    }

    
    public Long getId(){
        return id;
    }
    public void setId(Long id){
        this.id = id;
    }

    public String getProductName(){
        return this.productName;
    }
    public void setProductName(String productName){
        this.productName = productName;
    }

    public double getPrice(){
        return this.price;
    }
    public void setPrice(double price){
        this.price = price;
    }
    //product_name, price, the_date, store_name

}
