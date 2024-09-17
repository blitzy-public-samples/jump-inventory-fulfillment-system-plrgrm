/**
 * Validates an email address
 * @param email The email address to validate
 * @returns True if email is valid, false otherwise
 */
export function isValidEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Validates a product SKU
 * @param sku The SKU to validate
 * @returns True if SKU is valid, false otherwise
 */
export function isValidSKU(sku: string): boolean {
  const skuRegex = /^[A-Z0-9]{8,12}$/;
  return skuRegex.test(sku);
}