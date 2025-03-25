package com.java.Price_Watch.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.java.Price_Watch.model.CVSProduct;

@Repository
public interface CVSProductRepository extends JpaRepository<CVSProduct, Long> {
    // JpaRepository provides basic CRUD operations and additional JPA-specific methods
    // Add custom query methods if needed
} 