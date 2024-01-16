
# def payment_ipn(request):
#     inputData = request.GET
#     if inputData:
#         vnp = vnpay()
#         vnp.responseData = inputData.dict()
#         order_id = inputData['vnp_TxnRef']
#         amount = inputData['vnp_Amount']
#         order_desc = inputData['vnp_OrderInfo']
#         vnp_TransactionNo = inputData['vnp_TransactionNo']
#         vnp_ResponseCode = inputData['vnp_ResponseCode']
#         vnp_TmnCode = inputData['vnp_TmnCode']
#         vnp_PayDate = inputData['vnp_PayDate']
#         vnp_BankCode = inputData['vnp_BankCode']
#         vnp_CardType = inputData['vnp_CardType']
#         if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
#             # Check & Update Order Status in your Database
#             # Your code here
#             firstTimeUpdate = True
#             totalAmount = True
#             if totalAmount:
#                 if firstTimeUpdate:
#                     if vnp_ResponseCode == '00':
#                         print('Payment Success. Your code implement here')
#                     else:
#                         print('Payment Error. Your code implement here')

#                     # Return VNPAY: Merchant update success
#                     result = JsonResponse({'RspCode': '00', 'Message': 'Confirm Success'})
#                 else:
#                     # Already Update
#                     result = JsonResponse({'RspCode': '02', 'Message': 'Order Already Update'})
#             else:
#                 # invalid amount
#                 result = JsonResponse({'RspCode': '04', 'Message': 'invalid amount'})
#         else:
#             # Invalid Signature
#             result = JsonResponse({'RspCode': '97', 'Message': 'Invalid Signature'})
#     else:
#         result = JsonResponse({'RspCode': '99', 'Message': 'Invalid request'})

#     return result
		