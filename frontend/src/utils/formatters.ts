import { format, parseISO } from 'date-fns';

export function formatCurrency(amount: number, currencyCode: string): string {
  const formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currencyCode,
  });
  return formatter.format(amount);
}

export function formatDate(dateString: string): string {
  const parsedDate = parseISO(dateString);
  return format(parsedDate, 'MMMM d, yyyy');
}