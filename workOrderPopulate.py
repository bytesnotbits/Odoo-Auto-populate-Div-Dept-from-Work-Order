# The 'record' variable is the Sales Order Line that the user is editing.

# --- MASTER SWITCH: Only run if the intent is "Work Order" ---
# --- This should be changed to trigger on an ID number rather than a string which could change in the future ---
if record.x_studio_nisc_transaction_type == 'Work Order':

    # --- Check if a Work Order is selected ---
    if record.x_studio_work_order:
        
        work_order = record.x_studio_work_order
        gl_account_wo = env['x_gl_account'].search([('x_studio_api_code', '=', '2003.3')], limit=1)
        if gl_account_wo:
            record['x_studio_gl_account'] = gl_account_wo.id
            
        rulebook_entry = work_order.x_studio_work_order_type
        
        if rulebook_entry:
            if rulebook_entry.x_studio_gl_division:
                record['x_studio_gl_division'] = rulebook_entry.x_studio_gl_division.id
            if rulebook_entry.x_studio_gl_department:
                record['x_studio_gl_department'] = rulebook_entry.x_studio_gl_department.id
                
        if work_order.x_studio_exchange:
            record['x_studio_exchange'] = work_order.x_studio_exchange.id
            
    # --- Cleanup ---
    else:
        record['x_studio_gl_account'] = False
        record['x_studio_gl_division'] = False
        record['x_studio_gl_department'] = False
        record['x_studio_exchange'] = False
