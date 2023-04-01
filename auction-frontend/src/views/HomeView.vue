<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Auction App
        </p>
        <p class="subtitle">
          The Best Online Auction Experience
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Products</h2>
      </div>

      <!-- <ProductBox v-for="product in latestProducts" v-bind:key="product.id" v-bind:product="product" /> -->

    </div>
  </div>
</template>


<script>

export default {
  name: 'HomeView',
  data() {
    return {
    }
  },
  components: {
  },
  mounted() {
    document.title = 'Home | Auction App'
  },
  methods: {
  },
}
</script>