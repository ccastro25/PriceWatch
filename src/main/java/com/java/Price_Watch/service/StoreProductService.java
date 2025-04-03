package com.java.Price_Watch.service;

import com.java.Price_Watch.model.CVSProduct;
import com.java.Price_Watch.model.WalmartProduct;
import com.java.Price_Watch.repository.CVSProductRepository;
import com.java.Price_Watch.repository.WalmartProductRepository;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class StoreProductService {
    private final CVSProductRepository cvsRepository;
    private final WalmartProductRepository walmartRepository;

    public StoreProductService(
            CVSProductRepository cvsRepository,
            WalmartProductRepository walmartRepository) {
        this.cvsRepository = cvsRepository;
        this.walmartRepository = walmartRepository;
    }

    // CVS Operations
    public CVSProduct saveCVSProduct(String productName, double price) {
        CVSProduct product = new CVSProduct();
        product.setProductName(productName);
        product.setPrice(price);
        return cvsRepository.save(product);
    }

    public List<CVSProduct> getAllCVSProducts() {
        return cvsRepository.findAll();
    }

    public CVSProduct getCVSProductById(Long id) {
        return cvsRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("CVS Product not found with id: " + id));
    }

    public void deleteCVSProduct(Long id) {
        cvsRepository.deleteById(id);
    }

    public CVSProduct updateCVSProduct(Long id, String productName, double price) {
        CVSProduct product = getCVSProductById(id);
        product.setProductName(productName);
        product.setPrice(price);
        return cvsRepository.save(product);
    }

    // Walmart Operations
    public WalmartProduct saveWalmartProduct(String productName, double price) {
        WalmartProduct product = new WalmartProduct();
        product.setProductName(productName);
        product.setPrice(price);
        return walmartRepository.save(product);
    }

    public List<WalmartProduct> getAllWalmartProducts() {
        return walmartRepository.findAll();
    }

    public WalmartProduct getWalmartProductById(Long id) {
        return walmartRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Walmart Product not found with id: " + id));
    }

    public void deleteWalmartProduct(Long id) {
        walmartRepository.deleteById(id);
    }

    public WalmartProduct updateWalmartProduct(Long id, String productName, double price) {
        WalmartProduct product = getWalmartProductById(id);
        product.setProductName(productName);
        product.setPrice(price);
        return walmartRepository.save(product);
    }
} 