import { MenuRootItem } from 'ontimize-web-ngx';

import { CategoryCardComponent } from './Category-card/Category-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { MenuItemCardComponent } from './MenuItem-card/MenuItem-card.component';

import { MenuItemPromotionCardComponent } from './MenuItemPromotion-card/MenuItemPromotion-card.component';

import { MenuItemSupplierCardComponent } from './MenuItemSupplier-card/MenuItemSupplier-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { PromotionCardComponent } from './Promotion-card/Promotion-card.component';

import { RestaurantCardComponent } from './Restaurant-card/Restaurant-card.component';

import { ReviewCardComponent } from './Review-card/Review-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Category', name: 'CATEGORY', icon: 'view_list', route: '/main/Category' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'MenuItem', name: 'MENUITEM', icon: 'view_list', route: '/main/MenuItem' }
    
        ,{ id: 'MenuItemPromotion', name: 'MENUITEMPROMOTION', icon: 'view_list', route: '/main/MenuItemPromotion' }
    
        ,{ id: 'MenuItemSupplier', name: 'MENUITEMSUPPLIER', icon: 'view_list', route: '/main/MenuItemSupplier' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Promotion', name: 'PROMOTION', icon: 'view_list', route: '/main/Promotion' }
    
        ,{ id: 'Restaurant', name: 'RESTAURANT', icon: 'view_list', route: '/main/Restaurant' }
    
        ,{ id: 'Review', name: 'REVIEW', icon: 'view_list', route: '/main/Review' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CategoryCardComponent

    ,CustomerCardComponent

    ,EmployeeCardComponent

    ,MenuItemCardComponent

    ,MenuItemPromotionCardComponent

    ,MenuItemSupplierCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,PromotionCardComponent

    ,RestaurantCardComponent

    ,ReviewCardComponent

    ,SupplierCardComponent

];