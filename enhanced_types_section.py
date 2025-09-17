# Enhanced Types of Linked Lists section with perfect sum calculation
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import math
import time

def enhanced_types_of_linked_lists():
    st.markdown('<h1 class="main-header" style="margin-top: 0;">🔗 Types of Linked Lists</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #1e3c72; text-align: center; margin-bottom: 1.5rem;">🎯 Master All Linked List Variants</h2>
    <p style="font-size: 1.1em; text-align: center; color: #666; margin-bottom: 1rem;">
    Explore singly, doubly, and circular linked lists with interactive sum calculations and comprehensive theory.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced Sum calculation section with interactive examples
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #1e3c72; text-align: center; margin-bottom: 1.5rem;">🧮 Sum Calculation Mastery</h2>
    <p style="font-size: 1.1em; text-align: center; color: #666; margin-bottom: 1rem;">
    Master sum calculations across all linked list types with interactive examples and theory.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # Interactive sum calculator with visualization
    st.subheader("🧮 Interactive Sum Calculator")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        calc_type = st.selectbox("Choose list type for sum calculation:", 
                                ["Singly Linked", "Doubly Linked", "Circular Linked"])
        
        calc_input = st.text_input("Enter numbers (comma-separated):", "10, 20, 30, 40")
        
        if st.button("Calculate Sum", type="primary"):
            try:
                numbers = [int(x.strip()) for x in calc_input.split(",") if x.strip()]
                if numbers:
                    total = sum(numbers)
                    
                    # Enhanced results display
                    st.markdown(f"""
                    <div class="metric-card">
                    <div class="metric-value">{total}</div>
                    <div class="metric-label">{calc_type} Sum</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Statistics
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        st.metric("Count", len(numbers))
                    with col_b:
                        st.metric("Average", f"{total/len(numbers):.2f}")
                    with col_c:
                        st.metric("Max", max(numbers))
                    
                    # Visual representation
                    fig = go.Figure(data=[
                        go.Bar(x=[f"Node {i+1}" for i in range(len(numbers))], 
                               y=numbers,
                               marker_color='#4A90E2',
                               text=numbers,
                               textposition='auto')
                    ])
                    fig.update_layout(
                        title=f"{calc_type} Elements Visualization",
                        xaxis_title="Nodes",
                        yaxis_title="Values",
                        height=300
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Show step-by-step calculation
                    with st.expander("🔍 Step-by-step calculation"):
                        running_sum = 0
                        for i, num in enumerate(numbers):
                            running_sum += num
                            st.write(f"**Step {i+1}:** {running_sum-num} + {num} = **{running_sum}**")
                else:
                    st.warning("Please enter valid numbers")
            except ValueError:
                st.error("Please enter valid integers separated by commas")
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4>💡 Sum Tips</h4>
        <ul>
        <li><strong>Singly:</strong> Forward traversal only</li>
        <li><strong>Doubly:</strong> Can sum forward or backward</li>
        <li><strong>Circular:</strong> Must avoid infinite loops</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # Enhanced comparison with interactive elements
    st.subheader("⚡ Sum Algorithm Analysis")
    
    # Interactive comparison table
    sum_comparison_data = {
        'List Type': ['Singly Linked', 'Doubly Linked', 'Circular Linked'],
        'Time Complexity': ['O(n)', 'O(n)', 'O(n)'],
        'Implementation Difficulty': ['Easy', 'Easy', 'Moderate'],
        'Safety Concerns': ['None', 'None', 'Infinite loops'],
        'Optimization Potential': ['Low', 'Medium', 'Low'],
        'Best Use Case': ['Simple sums', 'Directional sums', 'Continuous sums']
    }
    
    df = pd.DataFrame(sum_comparison_data)
    st.dataframe(df, use_container_width=True)
    
    # Visual comparison
    metrics = ['Ease of Implementation', 'Safety', 'Performance']
    singly_scores = [9, 9, 8]
    doubly_scores = [7, 9, 7]
    circular_scores = [5, 6, 8]
    
    fig = go.Figure(data=[
        go.Radar(r=singly_scores, theta=metrics, fill='toself', name='Singly Linked', line_color='#4A90E2'),
        go.Radar(r=doubly_scores, theta=metrics, fill='toself', name='Doubly Linked', line_color='#E74C3C'),
        go.Radar(r=circular_scores, theta=metrics, fill='toself', name='Circular Linked', line_color='#9B59B6')
    ])
    
    fig.update_layout(title="Sum Calculation Comparison Radar", height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Enhanced Circular Linked List Theory with Sum Focus
    st.markdown("""
    <div class="section-card">
    <h3 style="color: #1e3c72; margin-bottom: 1rem;">🔄 Circular Linked List Deep Dive</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Enhanced Node Structure:**
        ```python
        class CircularNode:
            def __init__(self, data):
                self.data = data
                self.next = None
                self.visited = False  # For sum calculation safety
        ```

        **Sum Calculation Theory:**
        The key challenge in circular linked lists is preventing infinite loops during traversal.
        
        **Three Safe Sum Methods:**
        
        1. **Node Counter Method** (Recommended)
        ```python
        def safe_sum_with_count(head, size):
            total = 0
            current = head
            for i in range(size):
                total += current.data
                current = current.next
            return total
        ```
        
        2. **Starting Node Reference**
        ```python
        def safe_sum_with_reference(head):
            if not head:
                return 0
            total = head.data
            current = head.next
            while current != head:
                total += current.data
                current = current.next
            return total
        ```
        
        3. **Visited Flag Method**
        ```python
        def safe_sum_with_flags(head):
            total = 0
            current = head
            while current and not current.visited:
                current.visited = True
                total += current.data
                current = current.next
            # Reset flags
            reset_visited_flags(head)
            return total
        ```

        **Performance Analysis:**
        - **Time Complexity:** O(n) for all methods
        - **Space Complexity:** O(1) for counter/reference, O(n) for flags
        - **Safety:** Counter method is most reliable
        - **Memory:** Reference method most efficient
        """)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4>⚠️ Critical Sum Rules</h4>
        <ol>
        <li><strong>Never</strong> use NULL check</li>
        <li><strong>Always</strong> have termination condition</li>
        <li><strong>Track</strong> starting position</li>
        <li><strong>Count</strong> nodes if size known</li>
        <li><strong>Test</strong> with single node</li>
        </ol>
        </div>
        
        <div class="metric-card" style="margin-top: 1rem;">
        <div class="metric-value">3</div>
        <div class="metric-label">Safe Sum Methods</div>
        </div>
        
        <div class="feature-card" style="margin-top: 1rem; background: linear-gradient(135deg, #9B59B6 0%, #8E44AD 100%);">
        <h4>🔄 Circular Benefits</h4>
        <ul style="text-align: left; font-size: 0.9em;">
        <li>Natural for round-robin</li>
        <li>No end-of-list checks</li>
        <li>Continuous processing</li>
        <li>Memory efficient</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # Enhanced Visual Representation
    st.subheader("Enhanced Visual Representation")
    
    # Interactive circular list visualization
    st.markdown("""
    <div class="visual-diagram">
    <h4 style="margin-bottom: 1rem; color: #1e3c72;">🔄 Circular Sum Visualization</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Create interactive circular visualization
    demo_values = [10, 20, 30]
    fig = go.Figure()
    
    # Circular arrangement
    radius = 2
    angles = [2 * math.pi * i / len(demo_values) for i in range(len(demo_values))]
    node_x = [radius * math.cos(angle) for angle in angles]
    node_y = [radius * math.sin(angle) for angle in angles]
    
    # Add nodes
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        marker=dict(size=60, color='#9B59B6', line=dict(width=3, color='#8E44AD')),
        text=[f'{val}' for val in demo_values],
        textfont=dict(size=16, color='white', family="Arial Black"),
        name="Nodes",
        hovertemplate="<b>Value: %{text}</b><br>Sum so far: %{customdata}<extra></extra>",
        customdata=[sum(demo_values[:i+1]) for i in range(len(demo_values))]
    ))
    
    # Add circular arrows
    for i in range(len(demo_values)):
        next_i = (i + 1) % len(demo_values)
        # Arrow from current to next
        fig.add_annotation(
            x=node_x[next_i], y=node_y[next_i],
            ax=node_x[i], ay=node_y[i],
            xref='x', yref='y', axref='x', ayref='y',
            arrowhead=2, arrowsize=1.5, arrowwidth=3, 
            arrowcolor='#FF6B6B' if i < len(demo_values)-1 else '#9B59B6',
            showarrow=True
        )
    
    # Add sum annotation in center
    fig.add_annotation(
        x=0, y=0,
        text=f"Sum = {sum(demo_values)}",
        showarrow=False,
        font=dict(size=18, color='#1e3c72', family="Arial Black"),
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="#1e3c72",
        borderwidth=2
    )
    
    fig.update_layout(
        title="Circular Linked List Sum Calculation",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-3, 3]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-3, 3]),
        showlegend=False,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.code("""
Circular Sum Process:
Step 1: Start at Node(10), Sum = 10
Step 2: Move to Node(20), Sum = 30  
Step 3: Move to Node(30), Sum = 60
Step 4: Back to Node(10) - STOP! (Detected cycle)
Final Sum: 60
    """)

    # Enhanced real-world applications with interactive examples
    st.subheader("🌟 Real-World Sum Applications")
    
    # Interactive application selector
    app_type = st.selectbox("Choose application scenario:", 
                           ["Shopping Cart", "Game Scores", "Sensor Readings", "Financial Transactions"])
    
    if app_type == "Shopping Cart":
        st.markdown("""
        <div class="code-container">
        <div class="code-header">
        <span>🛒 Shopping Cart (Singly Linked)</span>
        </div>
        <div class="code-content">
class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None

def calculate_cart_total(cart_head):
    total = 0
    current = cart_head
    while current:
        total += current.price
        current = current.next
    return total

# Example: Apple($2) → Banana($1) → Orange($3) = $6
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive cart calculator
        st.write("**Try it yourself:**")
        items_input = st.text_input("Enter items and prices (format: item1:price1, item2:price2):", 
                                   "Apple:2, Banana:1, Orange:3")
        
        if st.button("Calculate Cart Total"):
            try:
                items = []
                total = 0
                for item_price in items_input.split(","):
                    if ":" in item_price:
                        name, price = item_price.strip().split(":")
                        price = float(price)
                        items.append((name.strip(), price))
                        total += price
                
                st.success(f"🛒 **Cart Total: ${total:.2f}**")
                for name, price in items:
                    st.write(f"- {name}: ${price:.2f}")
            except:
                st.error("Invalid format. Use: item1:price1, item2:price2")
    
    elif app_type == "Game Scores":
        st.markdown("""
        <div class="code-container">
        <div class="code-header">
        <span>🎮 Game Scores (Doubly Linked)</span>
        </div>
        <div class="code-content">
class ScoreNode:
    def __init__(self, score):
        self.score = score
        self.next = None
        self.prev = None

def calculate_total_score(head):
    total = 0
    current = head
    while current:
        total += current.score
        current = current.next
    return total

# Bidirectional: 100 ↔ 85 ↔ 92 ↔ 78 = 355
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    elif app_type == "Sensor Readings":
        st.markdown("""
        <div class="code-container">
        <div class="code-header">
        <span>🌡️ Sensor Readings (Circular Linked)</span>
        </div>
        <div class="code-content">
class SensorNode:
    def __init__(self, reading):
        self.reading = reading
        self.next = None

def calculate_average_reading(head, count):
    if not head:
        return 0
    
    total = 0
    current = head
    for i in range(count):
        total += current.reading
        current = current.next
        if current == head:  # Circular check
            break
    
    return total / count

# Circular sensors: 25.5° → 26.1° → 24.8° → (back to start)
        </div>
        </div>
        """, unsafe_allow_html=True)

    # Final comprehensive insights
    st.markdown("""
    <div class="section-card">
    <h3 style="color: #1e3c72; text-align: center; margin-bottom: 1rem;">🎆 Sum Calculation Mastery Summary</h3>
    
    <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #4CAF50;">✅</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Singly: Simple Forward</div>
    </div>
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #2196F3;">↔️</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Doubly: Bidirectional</div>
    </div>
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #9B59B6;">🔄</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Circular: Loop-Safe</div>
    </div>
    </div>
    
    <div class="highlight-box">
    <h4>💡 Universal Truth</h4>
    <p><strong>All linked list types have O(n) time complexity for sum calculation, but implementation safety varies significantly.</strong></p>
    <ul>
    <li><strong>Singly:</strong> Straightforward iteration until NULL</li>
    <li><strong>Doubly:</strong> Can optimize by choosing direction</li>
    <li><strong>Circular:</strong> Requires careful termination logic</li>
    </ul>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Continue to next section button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Master Operations Next →", key="master_operations", use_container_width=True, type="primary"):
            st.balloons()
            st.success("🎉 Great job! Moving to operations...")
            time.sleep(1)
            st.rerun()

if __name__ == "__main__":
    enhanced_types_of_linked_lists()