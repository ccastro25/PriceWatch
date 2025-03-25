package com.java.Price_Watch.service;

import com.java.Price_Watch.model.CVSProduct;
import com.java.Price_Watch.model.RiteAidProduct;
import com.java.Price_Watch.model.WalmartProduct;
import com.java.Price_Watch.repository.CVSProductRepository;
import com.java.Price_Watch.repository.RiteAidProductRepository;
import com.java.Price_Watch.repository.WalmartProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;

@Service
public class StoreProductService {
    
    private final CVSProductRepository cvsRepository;
    private final RiteAidProductRepository riteAidRepository;
    private final WalmartProductRepository walmartRepository;

    @Autowired
    public StoreProductService(CVSProductRepository cvsRepository,
                             RiteAidProductRepository riteAidRepository,
                             WalmartProductRepository walmartRepository) {
        this.cvsRepository = cvsRepository;
        this.riteAidRepository = riteAidRepository;
        this.walmartRepository = walmartRepository;
    }

    // CVS Operations
    public CVSProduct saveCVSProduct(String productName, double price) {
        CVSProduct product = new CVSProduct();
        product.setProductName(productName);
        product.setPrice(price);
        product.setDate(LocalDate.now());
        return cvsRepository.save(product);
    }

    public List<CVSProduct> getAllCVSProducts() {
        return cvsRepository.findAll();
    }

    public CVSProduct getCVSProductById(Long id) {
        return cvsRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("CVS Product not found with id: " + id));
    }

    // RiteAid Operations
    public RiteAidProduct saveRiteAidProduct(String productName, double price) {
        RiteAidProduct product = new RiteAidProduct();
        product.setProductName(productName);
        product.setPrice(price);
        product.setDate(LocalDate.now());
        return riteAidRepository.save(product);
    }

    public List<RiteAidProduct> getAllRiteAidProducts() {
        return riteAidRepository.findAll();
    }

    public RiteAidProduct getRiteAidProductById(Long id) {
        return riteAidRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("RiteAid Product not found with id: " + id));
    }

    // Walmart Operations
    public WalmartProduct saveWalmartProduct(String productName, double price) {
        WalmartProduct product = new WalmartProduct();
        product.setProductName(productName);
        product.setPrice(price);
        product.setDate(LocalDate.now());
        return walmartRepository.save(product);
    }

    public List<WalmartProduct> getAllWalmartProducts() {
        return walmartRepository.findAll();
    }

    public WalmartProduct getWalmartProductById(Long id) {
        return walmartRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Walmart Product not found with id: " + id));
    }

    // Delete Operations
    public void deleteCVSProduct(Long id) {
        cvsRepository.deleteById(id);
    }

    public void deleteRiteAidProduct(Long id) {
        riteAidRepository.deleteById(id);
    }

    public void deleteWalmartProduct(Long id) {
        walmartRepository.deleteById(id);
    }

    // Update Operations
    public CVSProduct updateCVSProduct(Long id, String productName, double price) {
        CVSProduct product = getCVSProductById(id);
        product.setProductName(productName);
        product.setPrice(price);
        return cvsRepository.save(product);
    }

    public RiteAidProduct updateRiteAidProduct(Long id, String productName, double price) {
        RiteAidProduct product = getRiteAidProductById(id);
        product.setProductName(productName);
        product.setPrice(price);
        return riteAidRepository.save(product);
    }

    public WalmartProduct updateWalmartProduct(Long id, String productName, double price) {
        WalmartProduct product = getWalmartProductById(id);
        product.setProductName(productName);
        product.setPrice(price);
        return walmartRepository.save(product);
    }
} 