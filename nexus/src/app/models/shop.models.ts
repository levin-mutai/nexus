export interface Shop {
  address: string;
  created_at: string;
  description: string;
  email: string;
  id: string;
  logo: string | null;
  name: string;
  owner: string;
  phone: string;
  updated_at: string;
}

export interface ShopCreate {
  name: string;
  address: string;
  phone: string;
  email: string;
  description: string;
}

export interface Product {
  name: string;
  price: number;
  description: string;
  stock: number;
  measurement: string;
  shop: string;
  category: string;
}
