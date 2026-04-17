/* FORWARD MOTION PRODUCT DATABASE STRUCTURE */

-- 1. Create Tables for Organization
CREATE TABLE product_catalog (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    subcategory TEXT,
    hcpcs_codes TEXT
);

CREATE TABLE technical_specs (
    product_id INTEGER,
    shell_material TEXT,
    heel_cup_depth TEXT,
    top_cover TEXT,
    special_features TEXT,
    FOREIGN KEY (product_id) REFERENCES product_catalog(product_id)
);

-- 2. Sample Data for AI Reference
-- Custom Orthotic Entry [cite: 136, 140, 145]
INSERT INTO product_catalog VALUES (1, 'FM Integrated', 'Custom Orthotic', 'Functional', 'L3000, L3010');
INSERT INTO technical_specs VALUES (1, '3/16" Polypropylene', '12mm', 'Marine Grade Vinyl', 'Integrated Heel Post');

-- Custom Brace Entry [cite: 405, 445, 459]
INSERT INTO product_catalog VALUES (2, 'Articulated Gauntlet', 'Custom Brace', 'BOSS Gauntlet', 'L1970, L2820, L2330');
INSERT INTO technical_specs VALUES (2, '1/8" Polypropylene', '25mm', 'Leather', 'Tamarack Hinge System');

-- Prefab Entry [cite: 611]
INSERT INTO product_catalog VALUES (3, 'Diabetic Insole', 'Prefabricated', 'Accommodative', 'A5500');
INSERT INTO technical_specs VALUES (3, 'Multi-Durometer', 'N/A', 'Bilaminate', 'Medicare Compliant');